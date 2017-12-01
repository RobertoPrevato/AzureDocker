package main

import (
	"bytes"
	"fmt"
	"net/http"
	"os"
	"strconv"
	"time"

	"github.com/golang/groupcache/lru"
)

var cache *lru.Cache

func handler(w http.ResponseWriter, r *http.Request) {
	var resp []byte

	respSize := r.URL.Query().Get("s")
	if respSize != "" {
		s, err := strconv.Atoi(respSize)
		if err != nil {
			resp = []byte("Invalid query: cannot parse size")
		} else {
			if s > 101 {
				resp = []byte("Invalid query: exceeds 101")
			} else {
				val, ok := cache.Get(s)
				if ok {
					resp = val.([]byte)
				} else {
					resp = bytes.Repeat([]byte{'X'}, s*1000)
					cache.Add(s, resp)
				}
			}
		}
	} else {
		resp = []byte("Hello World, from Go! " + time.Now().Format(time.RFC3339Nano))
	}

	w.Write(resp)
}

func main() {
	cache = lru.New(10)
	http.HandleFunc("/", handler)
	var port = os.Getenv("SERVER_PORT")
	if port == "" {
		port = "25000"
	}
	fmt.Println("Serving on :" + port)
	http.ListenAndServe(":"+port, nil)
}

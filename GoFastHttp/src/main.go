package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
	"time"

	"github.com/golang/groupcache/lru"
	"github.com/valyala/fasthttp"
)

var cache *lru.Cache

func main() {
	cache = lru.New(10)
	flag.Parse()

	var port = os.Getenv("SERVER_PORT")
	if port == "" {
		port = ":80"
	}
	fmt.Println("Serving on " + port)

	h := requestHandler

	if err := fasthttp.ListenAndServe(port, h); err != nil {
		log.Fatalf("Error in ListenAndServe: %s", err)
	}
}

func requestHandler(ctx *fasthttp.RequestCtx) {
	var message string
	var query = ctx.QueryArgs()

	var size = query.GetUintOrZero("s")

	if size > 0 {
		sizeString := strconv.Itoa(size)

		if size > 101 {
			message = "Invalid query: exceeds 101"
		} else {
			val, ok := cache.Get(sizeString)
			if ok {
				message, ok = val.(string)
			} else {
				message = strings.Repeat("X", size*1000)
				cache.Add(sizeString, message)
			}
		}
	} else {
		message = "Hello World, from Go, using fast http! " + time.Now().Format(time.RFC3339Nano)
	}

	fmt.Fprintf(ctx, message)
}

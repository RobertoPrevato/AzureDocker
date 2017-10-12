package main

import (
	"fmt"
	"net/http"
	"os"
	"time"
)

func handler(w http.ResponseWriter, r *http.Request) {
	var resp []byte
	var x = "Hello World, from Go! " + time.Now().Format(time.RFC3339Nano)
	resp = []byte(x)
	w.Write(resp)
}

func main() {
	http.HandleFunc("/", handler)
	var port = os.Getenv("SERVER_PORT")
	if port == "" {
		port = "25000"
	}
	fmt.Println("Serving on :" + port)
	http.ListenAndServe(":"+port, nil)
}

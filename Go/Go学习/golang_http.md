# Go中的http使用

```GO
package main

import (
	"fmt"
	"net/http"
	"io/ioutil"
	"strings"
	"net/url"
)

func httpGet(){
	resp, err := http.Get("http://www.baidu.com")
	if err != nil {
		fmt.Println(err)
		return
	}
	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(string(body))
}

func httpPost(){
	resp, err := http.Post("http://www.baidu.com",
"application/x-www-form-urlencoded",
strings.NewReader("name=zzr"))
if err != nil {
	fmt.Println(err)
	return
}
defer resp.Body.Close()
body, err := ioutil.ReadAll(resp.Body)
if err != nil {
	fmt.Println(err)
	return
}
fmt.Println(string(body))
}

func httpPostForm(){
	resp, err := http.PostForm("http://www.baidu.com",
	url.Values{"key":{"value"}, "id":{"123"}})

	if err != nil {
		fmt.Println(err)
		return
	}
	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(string(body))
}

func httpDo(){
	client := &http.Client{}

	req, err := http.NewRequest("POST", "http://www.baidu.com",strings.NewReader("name=zzr"))
	if err != nil{
		fmt.Println(err)
		return
	}
	req.Header.Set("Content-Type", "application/x-www.form-urlencoded")
	req.Header.Set("Cookie", "name=ben")

	resp, err := client.Do(req)

	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(string(body))
}
func main(){
	httpPost()	
}
```
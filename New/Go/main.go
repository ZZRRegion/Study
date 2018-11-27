package main

import (
	"fmt"
	"io/ioutil"
	"os/exec"
)

func main() {
	cmd := exec.Command("Test.exe", "hello")
	stdout, err := cmd.StdoutPipe()
	if err != nil {
		fmt.Println(err)
	}
	defer stdout.Close()
	if err := cmd.Start(); err != nil {
		fmt.Println(err)
	}
	opBytes, err := ioutil.ReadAll(stdout)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(string(opBytes))
}

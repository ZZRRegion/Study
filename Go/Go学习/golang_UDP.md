# Go语言中的UDP应用
Go语言中使用UDP是很方便的，net包提供了UDP和TCP的功能，这里使用UDP做了一个UDP广播，然后接收各个设备的返回信息。实现起来很快，总体感觉比使用C#中的UDP更优雅，简洁。

```GO
package main

import (
	"fmt"
	"net"
	"time"
	"strings"
	"reflect"
)

func recvUDPMsg(conn *net.UDPConn){
	fmt.Println("进入了")
	for{
		var buf [1024] byte
		n, raddr, err := conn.ReadFromUDP(buf[0:])
		if err != nil{
			fmt.Println(err)
			return
		}
		content := string(buf[0:n])
		hmis := strings.Split(content, ",")
		hmi := new(HMIModel)
		hmi.ReflectInfo(hmis)
		fmt.Println(hmi)
		
		_, err = conn.WriteToUDP([]byte("hello world"), raddr)
		if err != nil {
			fmt.Println(err)
		}
	}

}
type HMIModel struct{
	company string
	ip string
	hostname string
	pncode string
	versoft string
	projectname string
}
func (this HMIModel) ReflectInfo(hmis []string){
	f := reflect.TypeOf(this)	
	v := reflect.ValueOf(this)
	for i := 0; i < f.NumField(); i++{
		for j := 0; j < len(hmis); j++{
			contents := strings.Split(hmis[i], "=")
			if contents[0] == f.Field(i).Name{
				v.Field(i).SetString(contents[1])
				break
			}

		}
	}
}

func main(){
	fmt.Println("开始了")
	udp_addr, err := net.ResolveUDPAddr("udp", "192.168.200.221:1100")
	if err != nil{
		fmt.Println(err)
		return
	}
	conn, err := net.ListenUDP("udp", udp_addr)
	if err != nil {
		fmt.Println(err)
		return
	}

	go recvUDPMsg(conn)
	raddr := net.UDPAddr{
		IP: net.ParseIP("255.255.255.255"),
		Port: 3366,
	}
	for{
		conn.WriteToUDP([]byte("hello world"), &raddr)

		time.Sleep(3 * time.Second)
	}
}
```
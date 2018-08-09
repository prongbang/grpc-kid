build-hello:
	protoc -I. helloworld/helloworld.proto --go_out=plugins=grpc:.

build-ping:
	protoc -I. pingpong/pingpong.proto --go_out=plugins=grpc:.

hello-server:
	go run greeter_server/main.go
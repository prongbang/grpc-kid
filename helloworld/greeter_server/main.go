package main

import (
	"context"
	"log"
	"net"
	"time"

	"google.golang.org/grpc/reflection"

	pb "github.com/prongbang/grpc-kid/helloworld/helloworld"
	"github.com/prongbang/grpc-kid/helloworld/pingpong"
	"google.golang.org/grpc"
)

const port = ":50051"

// server is used to implement helloworld.GreetrServer
type server struct{}

func (s *server) SayHello(ctx context.Context, in *pb.HelloRequest) (*pb.HelloResponse, error) {
	log.Printf("Request: %s", in.Name)
	return &pb.HelloResponse{Message: "Hello " + in.Name}, nil
}

func (s *server) SayHelloAgain(ctx context.Context, in *pb.HelloRequest) (*pb.HelloResponse, error) {
	return &pb.HelloResponse{Message: "Hello again " + in.Name}, nil
}

func main() {

	// Set up a connection to the pingpong server
	conn, err := grpc.Dial("localhost:50052", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	c := pingpong.NewPingpongerClient(conn)

	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()
	r, err := c.Ping(ctx, &pingpong.PingRequest{Name: "Ping"})
	if err != nil {
		log.Fatalf("could not pingpong: %v", err)
	}
	log.Printf("Pingpong: %s", r.Message)

	// Listener the server
	lis, err := net.Listen("tcp", port)
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterGreeterServer(s, &server{})

	// Register reflection service on gRPC server.
	reflection.Register(s)
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}

}

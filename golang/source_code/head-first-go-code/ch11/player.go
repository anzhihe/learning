package main

import "github.com/headfirstgo/gadget"

type Player interface {
	Play(string)
	Stop()
}

func TryOut(player Player) {
	player.Play("Test Track")
	player.Stop()
	recorder, ok := player.(gadget.TapeRecorder)
	if ok {
		recorder.Record()
	}
}

func main() {
	TryOut(gadget.TapeRecorder{})
	TryOut(gadget.TapePlayer{})
}

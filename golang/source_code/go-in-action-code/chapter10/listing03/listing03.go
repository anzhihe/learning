// Sample program demonstrating interface composition.
package main

import (
	"errors"
	"fmt"
	"io"
	"math/rand"
	"time"
)

func init() {
	rand.Seed(time.Now().UnixNano())
}

// =============================================================================

// Data is the structure of the data we are copying.
type Data struct {
	Line string
}

// =============================================================================

// Puller declares behavior for pulling data.
type Puller interface {
	Pull(d *Data) error
}

// Storer declares behavior for storing data.
type Storer interface {
	Store(d Data) error
}

// PullStorer declares behavior for both pulling and storing.
type PullStorer interface {
	Puller
	Storer
}

// =============================================================================

// Xenia is a system we need to pull data from.
type Xenia struct{}

// Pull knows how to pull data out of Xenia.
func (Xenia) Pull(d *Data) error {
	switch rand.Intn(10) {
	case 1, 9:
		return io.EOF

	case 5:
		return errors.New("Error reading data from Xenia")

	default:
		d.Line = "Data"
		fmt.Println("In:", d.Line)
		return nil
	}
}

// Pillar is a system we need to store data into.
type Pillar struct{}

// Store knows how to store data into Pillar.
func (Pillar) Store(d Data) error {
	fmt.Println("Out:", d.Line)
	return nil
}

// =============================================================================

// System wraps Xenia and Pillar together into a single system.
type System struct {
	Xenia
	Pillar
}

// =============================================================================

// pull knows how to pull bulks of data from any Puller.
func pull(p Puller, data []Data) (int, error) {
	for i := range data {
		if err := p.Pull(&data[i]); err != nil {
			return i, err
		}
	}

	return len(data), nil
}

// store knows how to store bulks of data from any Storer.
func store(s Storer, data []Data) (int, error) {
	for i, d := range data {
		if err := s.Store(d); err != nil {
			return i, err
		}
	}

	return len(data), nil
}

// Copy knows how to pull and store data from any System.
func Copy(ps PullStorer, batch int) error {
	data := make([]Data, batch)

	for {
		i, err := pull(ps, data)
		if i > 0 {
			if _, err := store(ps, data[:i]); err != nil {
				return err
			}
		}

		if err != nil {
			return err
		}
	}
}

// =============================================================================

func main() {

	// Initialize the system for use.
	sys := System{
		Xenia:  Xenia{},
		Pillar: Pillar{},
	}

	if err := Copy(&sys, 3); err != io.EOF {
		fmt.Println(err)
	}
}

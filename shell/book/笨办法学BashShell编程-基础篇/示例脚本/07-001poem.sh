#!/bin/bash
# 打印一首诗

Line[1]="Moonlight before my bed,"
Line[2]="Could it be frost instead?"
Line[3]="Head up, I watch the moon;"
Line[4]="Head down, I think of home."

Attrib[1]="Li Bai"
Attrib[2]="Quiet Night Thoughts"

echo
for index in 1 2 3 4
do
  printf "  %s\n" "${Line[index]}"
done

echo
for index in 1 2
do
  printf "  %s\n" "${Attrib[index]}"
done
exit 0

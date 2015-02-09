# gooey-interpreter

##Menus
```
make Menu m with options file edit view.
```
```
make Menu file with text "File", options "Save":saveAction.
```

##Positioning
```
make Window w with size (10,10).
```
Creates a 10 X 10 window where each cell is a tkinter Frame with height=100, width=100.
```
make Button b with positition (2,5).
```
Place button a row 2, column 5.

##Images
```
make Image i with source "apple.gif", position (2,5).
```
Tkinter only supports .gif files.
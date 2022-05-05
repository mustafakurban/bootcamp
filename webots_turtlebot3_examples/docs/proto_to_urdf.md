### proto2urdf package provided by webots simulator.

```text
Convert a PROTO file to URDF, WBO, or WRL file

Options:
  -h, --help            Displays help on commandline options.
  --help-all            Displays help including Qt specific options.
  -t <type>             Output type (URDF, WBO, or WRL).
  -o <output>           Path to the output file.
  -p <parameter=value>  Override default PROTO parameters.

Arguments:
  input                 Path to the input PROTO file.
```   


### Example usage


```bash
webots convert -t URDF TurtleBot3Burger.proto
```
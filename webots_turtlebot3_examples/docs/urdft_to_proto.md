


### Urdf to Webots(Proto)

    
> Python package provided by cyberobotics
[urdf2webots](https://github.com/cyberbotics/urdf2webots)

#### installation

```
pip install urdf2webots
```


#### Usage

```bash
python -m urdf2webots.importer --input=someRobot.urd[--output=outputFile] [--normal] [--box-collision] [--tool-slot=linkName] [--help]
```   

### Sample conversion process

```bash
python3 -m urdf2webots.importer --input=tb3_burger_will_be_converted.urdf --disable-mesh-optimization
```

> A similar output is expected.
------------------------------
> Robot name: tb3_burger_converted
>
> Root link: base_footprint
>
> There are 7 links, 6 joints and 0 sensors 


Let's start the simulation

One of the expected errors is the scale error. To solve this problem, go into the proto file and add the following line to the top of the block containing the mesh file (parameters can be changed upon request).

```xml
scale 0.001 0.001 0.001
```

> Note : Names of joints required for differential drive
It is the name given to the rotational motor.



#### warnings and solutions

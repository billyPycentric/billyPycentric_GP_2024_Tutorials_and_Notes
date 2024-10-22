# FLutter Notes   
Takes inspiration from React , the UI is Based on widgets    
~~~
import 'package:flutter/material.dart';

void main() {
  runApp(
    const Center(
      child: Text(
        'Hello, world!',
        textDirection: TextDirection.ltr,
      ),
    ),
  );
}
~~~    
simple Hello World App -> uses void to call the runApp, This is whether the root widget is initialized , the function takes in a widget ***Center*** as Its Child and another ***Text*** widget , Always use const for the root widget   
### Basic Widgets   
* Text   
* Row,Column   
* Stack   
* Container   
Difference between MaterialApp and Scaffold   
* Material App covers the struture for the entire app , while scaffold only covers a structure for a certain page .i.e The Material App is the Entire House Structure while Scaffold is the room Structure    
### Structuring AppBar   
1.Need a Class   
~~~
class MyAppBar extends StatelessWidget{
# After you will need a constructor with a const key word
const MyAppBar({required this.titile , super.key});

final Widget title;   

# Now the override
@override 
Widget build(VuildContext ctx){

return Your Widget
}
~~~    
## Handling Gestures   
Here is Just Basically interaction , but not with stateful widgets. , One of the methods you can use is ***Gesture Detector***    
Here is how you would use the Widget :   
~~~
GestureDetector(
      onTap: () {
        print('MyButton was tapped!');
      },
      child: Container(
        # Container Chars        ),
        child: # Child attr
      ),
    );
~~~    
## Introduction to Now ***StateFul-Widgtes***      
Here basically we have widgtes that change in response to user interaction    
#### Here is the basic Example   
~~~
class Counter extends StatefulWidget {

  const Counter({super.key});

  @override
  State<Counter> createState() => _CounterState();
}
~~~   
So here We have a counter Class , which extends StatefulWidget class    
Giving it a constructor and an optional key   
Then overide the State<Counter> createState() => _CounterState()    
#### What yoou will need to create a stateful application    
1. A value/Variable you want to keep state for/of(A container or anything you want)   
2.  Create a Class for it which returns the _var/valState()   
3. Create the _var/valState() Class which extends the State<var/val>   
4. The _var/valState() Class is the one stores everything   
### Example   
1.   
~~~
class Counter extends StatefulWidget {

  const Counter({super.key});

  @override
  State<Counter> createState() => _CounterState();
}
~~~    
2.   
~~~
class _CounterState extends State<Counter> {
  int _counter = 0;

  void _increment() {
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    // This method is rerun every time setState is called,
    // for instance, as done by the _increment method above.
    // The Flutter framework has been optimized to make
    // rerunning build methods fast, so that you can just
    // rebuild anything that needs updating rather than
    // having to individually changes instances of widgets.
    return Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: <Widget>[
        ElevatedButton(
          onPressed: _increment,
          child: const Text('Please press the Button'),
        ),
        const SizedBox(width: 16),
        Text('How many Time: $_counter'),
      ],
    );
  }
}

~~~   

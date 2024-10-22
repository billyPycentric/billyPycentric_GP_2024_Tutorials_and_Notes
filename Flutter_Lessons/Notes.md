# Flutter Notes -> The Second Comming
## Re-Introduction to Flutter   
MaterialApp -> is widget Navigator , basically helps you to navigate widgets , give the Structure
~~~dart
void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp();
  }
}

~~~   
This will show a blank screen because it has nothing in it   
if you add Scafold under the Material App , it will still have nothing -> And Scafold basic that provides visual framework for the Material Design   
### Addons on Columns/Rows   
***mainAxisAlignment*** , Helps you to move your columns/rows  
   
~~~dart
mainAxisAlignment: MainAxisAlignment.center
~~~   
### Expanded Widgets   
Help with size , easier to conf/change. i.e use **flex** for ratios      
### ListView   
scrolable columns/list   
~~~dart
ListView(

// Code here
);
~~~    
use ListView.Builder   
~~~dart

ListView.builder(

itemCount:6,
itemBuilder: (context,index) => ListTile(
title:Text(index.toString))
)


~~~   

### GridView   
~~~dart
GridView.builder(
itemCount = 64 /// For chess board 8X8
gridDeligate:SliverGridDeligateWithFixedCrossAsixCount(crossAxisCount:8),
itemBuilder: (context,index) => Container(color:,margin:EdgeInsets.all(2)) 

)
~~~

### Stack   
Also has children , just bsically stacking containers ontop of each other   

### GestureDetector
Wrap Everything under gesture detector      
~~~dart  

GestureDetector(
ontap: print("tapped the Button");

// Your widget here
);
~~~   
## Navigation   
Is basically moving from one page to another   
1. First need to import the function/package the page belongs to   
2. Call the function / widget   
3 . Create the navigation   
=> import "package:"nameofDir/.. /file.dart""   
=> homePage();   
=> have a button or anything that can be pressed   
onPressed(){

Navigator.push(context, MaterialPageRoute(builder:(context) => --Page))
}   
~~~dart

Center(
        child: ElevatedButton(
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => SecondPage(),
                ),
              );
            },
            child: Text("Tap Me !!!")),
      ),
~~~


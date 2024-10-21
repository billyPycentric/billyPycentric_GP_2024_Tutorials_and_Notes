// ignore_for_file: prefer_const_constructors

import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        backgroundColor: Colors.deepPurple[300],
        appBar: AppBar(
          title: Center(child: Text("My App")),
          backgroundColor: Colors.deepPurple,
          leading: IconButton(onPressed: () {}, icon: Icon(Icons.menu)),
          actions: [IconButton(onPressed: () {}, icon: Icon(Icons.webhook))],
        ),
        body: Column(
          
          children: [
            // Col1
            Container(
              height: 200,
              width: 200,
              color: Colors.deepPurple[400],
            ),

            // Col2
            Container(
              height: 200,
              width: 200,
              color: Colors.deepPurple[200],
            ),
            // Col3
            Container(
              height: 200,
              width: 200,
              color: Colors.deepPurple[100],
            ),
            
          ],
        ),
      ),
    );
  }
}

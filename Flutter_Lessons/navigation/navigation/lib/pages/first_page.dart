import 'package:flutter/material.dart';
import 'package:navigation/pages/second_page.dart';

class FirstPage extends StatelessWidget {
  const FirstPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Center(child: Text("First Page")),
        backgroundColor: Colors.deepPurple,
        leading: Icon(Icons.email),
      ),
      body: Center(
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
    );
  }
}

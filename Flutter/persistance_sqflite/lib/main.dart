import 'dart:async';

import 'package:flutter/widgets.dart';
import 'package:path/path.dart';
import 'package:sqflite/sqflite.dart';

void main() async {
  // Avoid errors caused by flutter upgrade.
  // Importing 'package:flutter/widgets.dart' is required.
  WidgetsFlutterBinding.ensureInitialized();
  // Open the database and store the reference.
  final database = openDatabase(
    // Set the path to the database. Note: Using the `join` function from the
    // `path` package is best practice to ensure the path is correctly
    // constructed for each platform.
    join(await getDatabasesPath(), 'pycentric.db'),
    // When the database is first created, create a table to store dogs.
    onCreate: (db, version) {
      // Run the CREATE TABLE statement on the database.
      return db.execute(
        'CREATE TABLE employees(id INTEGER PRIMARY KEY, name TEXT, surname TEXT ,description Text)',
      );
    },
    // Set the version. This executes the onCreate function and provides a
    // path to perform database upgrades and downgrades.
    version: 1,
  );

  // Define a function that inserts dogs into the database
  Future<void> insertEmployees(Employees employee) async {
    // Get a reference to the database.
    final db = await database;

    // Insert the Dog into the correct table. You might also specify the
    // `conflictAlgorithm` to use in case the same dog is inserted twice.
    //
    // In this case, replace any previous data.
    await db.insert(
      'employees',
      employee.toMap(),
      conflictAlgorithm: ConflictAlgorithm.replace,
    );
  }

  // A method that retrieves all the dogs from the dogs table.
  Future<List<Employees>> employees() async {
    // Get a reference to the database.
    final db = await database;

    // Query the table for all the dogs.
    final List<Map<String, Object?>> employeeMaps = await db.query('employees');

    // Convert the list of each dog's fields into a list of `Dog` objects.
    return [
      for (final {
            'id': id as int,
            'name': name as String,
            'surname': surname as String,
            'description': desciption as String
          } in employeeMaps)
        Employees(id: id, name: name, surname: surname, description:desciption),
    ];
  }

  // Create a Dog and add it to the dogs table
  var abongile = Employees(
    id: 0,
    name: 'Abongile',
    surname: "Billy",
    description: "He is a Male"
  );
  var khanyi = Employees(
      id: 1,
      name: 'Khayisa',
      surname: "M",
      description: "SHe is a FeMale"
  );
  var vhutali = Employees(
      id: 2,
      name: 'Vhutali',
      surname: "T",
      description: "He is a Male"
  );

  await insertEmployees(abongile);
  await insertEmployees(vhutali);
  await insertEmployees(khanyi);

  // Now, use the method above to retrieve all the dogs.
  print(await employees()); // Prints a list that include Fido.

  // // Print the updated results.
  // print(await dogs()); // Prints Fido with age 42.
  //
  // // Delete Fido from the database.
  // await deleteEmp(fido.id);
  //
  // // Print the list of dogs (empty).
  // print(await emp());
}

class Employees {
  final int id;
  final String name;
  final String surname;
  final String description;

  Employees({
    required this.id,
    required this.name,
    required this.surname,
    required this.description
  });

  // Convert a Dog into a Map. The keys must correspond to the names of the
  // columns in the database.
  Map<String, Object?> toMap() {
    return {
      'id': id,
      'name': name,
      'surname' : surname,
      'description': description
    };
  }

  // Implement toString to make it easier to see information about
  // each dog when using the print statement.
  @override
  String toString() {
    return 'Employees{id: $id, name: $name, surname: $surname ,description : $description}';
  }
}

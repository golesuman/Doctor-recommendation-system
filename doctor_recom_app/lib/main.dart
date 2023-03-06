import 'package:doctor_recom_app/home_screen.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Doctor Recommendation System',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.blue,
        inputDecorationTheme: InputDecorationTheme(
          enabledBorder: OutlineInputBorder(
            borderRadius: BorderRadius.circular(16),
          ),
          focusedBorder: OutlineInputBorder(
            borderRadius: BorderRadius.circular(16),
            borderSide: const BorderSide(
              color: Colors.blue,
            ),
          ),
          fillColor: const Color(0xFFF5F6F7),
          filled: true,
          floatingLabelBehavior: FloatingLabelBehavior.never,
          labelStyle: const TextStyle(color: Color(0xFF8E8E8E)),
          iconColor: const Color(0xFF8E8E8E),
          hintStyle: const TextStyle(color: Color(0xFF8E8E8E)),
        ),
      ),
      home: const HomeScreen(),
    );
  }
}

import 'dart:convert';
import 'package:http/http.dart' as http;

class PredictionService {
  final String baseUrl = "http://127.0.0.1:8000"; // Replace with your deployed API URL

  Future<double?> getPrediction(int hoursStudied, int attendance, int previousScores) async {
    final url = Uri.parse("$baseUrl/predict");
    final response = await http.post(
      url,
      headers: {"Content-Type": "application/json"},
      body: jsonEncode({
        "Hours_Studied": hoursStudied,
        "Attendance": attendance,
        "Previous_Scores": previousScores,
      }),
    );

    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      return data['prediction'];
    } else {
      print("Error: ${response.body}");
      return null;
    }
  }
}
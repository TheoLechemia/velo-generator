// Les vélos 6 à 10 sont branchés sur les entrées A0->A4 de la carte 2
int analogIn[5] = {A0,A1,A2,A3,A4};
// Fonction de lecture des pins analogiques et de calcul de l'intensité
int amplitude(int pin){
  int a = analogRead(pin) - 512; // Le 0 du capteur est au milieu de l'échelle [0-1024]
  float b = abs((a / 512.0) * 20.0); // Carte 20 Ampères
  int b2 = int(b);
  Serial.print(b2);
  delay(200); // Temporistation pour ne pas saturer la carte
  }
//Initialisation
void setup(){
  Serial.begin(9600);
}
//Lecture et envoi des valeurs à la vitesse de l'arduino
void loop(){
  Serial.print("Velo2;");
  amplitude(analogIn[0]);
  Serial.print(",");
  amplitude(analogIn[1]);
  Serial.print(",");
  amplitude(analogIn[2]);
  Serial.print(",");
  amplitude(analogIn[3]);
  Serial.print(",");
  amplitude(analogIn[4]);
  Serial.println();
}

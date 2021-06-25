// Les vélos 1 à 5 sont branchés sur les entrées A0->A4 de la carte 1
int analogIn[5] = {A0,A1,A2,A3,A4};
// Fonction de lecture des pins analogiques et de calcul de l'intensité
int amplitude(int pin){
  int nb_mesure = 100;
  int moyenne=0;
  int nit=0;
  int a = analogRead(pin) - 512;
  float b = abs((a / 512.0) * 20.0);
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
  Serial.print("Velo1;");
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

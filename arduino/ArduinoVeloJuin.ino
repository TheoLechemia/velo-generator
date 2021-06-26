// Les vélos 1 à 5 sont branchés sur les entrées A0->A4 de la carte 1
int analogIn[5] = {A0,A1,A2,A3,A4};
int TenAmps[10];
int nmoy = 1000; //Moyennage
// Fonction de lecture des pins analogiques et de calcul de l'intensité
int amplitude(int pin){
  int nit=0;
  int a = analogRead(pin) - 512;
  float b = 12*abs((a / 512.0) * 20.0);
  return b;
  }
    int moyandceil(float valu){
      int A=int(valu/nmoy-10);
   if (A>0)
   {
    return A;
   }
else
   {
return 0;
   }
}
//Initialisation
void setup(){
  Serial.begin(9600);
}
//Lecture et envoi des valeurs à la vitesse de l'arduino
void loop(){
  float v1=0.,v2=0.,v3=0.,v4=0.,v5=0.;
  for (int i = 0; i <= nmoy; i++) {
      v1= amplitude(analogIn[0])+v1;
      v2= amplitude(analogIn[1])+v2;
      v3= amplitude(analogIn[2])+v3;
      v4= amplitude(analogIn[3])+v4;
      v5= amplitude(analogIn[4])+v5;
    }
  Serial.print("Velo2;");
   Serial.print(moyandceil(v1));
  Serial.print(",");
   Serial.print(moyandceil(v2));
  Serial.print(",");
   Serial.print(moyandceil(v3));
  Serial.print(",");
   Serial.print(moyandceil(v4));
  Serial.print(",");
   Serial.print(moyandceil(v5));
  Serial.println();
}

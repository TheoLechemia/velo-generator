
int NbMoy = 40; // Nombre d'itération pour le filtrage
double AmpMax=30.0; // Intensité max admissible par le capteur
int analogIn[5] = {A0,A1,A2,A3,A4};
double Amp1; 
double Amp2; 
double Amp3; 
double Amp4; 
double Amp5;
double CarteOne[5];
double valeurBase[5];
int i=0;
int velo;
int moyenne=0;
void setup()
{
  Serial.begin(9600);
  Serial.println("Initialisation");
  delay(100);
  for ( velo = 0; velo < 5; velo++ )
    {
      moyenne=0;
      for( i = 0; i < NbMoy; i++ )
      {
          moyenne = moyenne + analogRead(analogIn[velo]);
      }
      valeurBase[velo] = moyenne / NbMoy;
      delay(200);
    }
}

void loop()
{
  Serial.print("Carte1;");
 //Velo 1
    moyenne = 0;
    for( i = 0; i < NbMoy; i++ )
    {
        moyenne = moyenne + analogRead(A0);
    }
    moyenne = moyenne / NbMoy;
    Amp1 = (valeurBase[0] - moyenne ) / AmpMax;
    CarteOne[1] = Amp1;
   // Serial.print("\t Velo1:");
    Serial.print(Amp1,1);
    Serial.print(",");

//Velo 2
    moyenne = 0;
    for( i = 0; i < NbMoy; i++ )
    {
        moyenne = moyenne + analogRead(A1);
    }
    moyenne = moyenne / NbMoy;
    Amp2 = (valeurBase[1] - moyenne ) / AmpMax;
    CarteOne[2] = Amp2;
    //Serial.print("\t Velo2:"); 
    Serial.print(Amp2,1);
    Serial.print(",");

//Velo 3
    moyenne = 0;
    for( i = 0; i < NbMoy; i++ )
    {
        moyenne = moyenne + analogRead(A2);
    }
    moyenne = moyenne / NbMoy;
    Amp3 = (valeurBase[2] - moyenne ) / AmpMax;
    CarteOne[3] = Amp3;
    //Serial.print("\t Velo3:"); 
    Serial.print(Amp3,1);
    Serial.print(",");
//Velo 4
    moyenne = 0;
    for( i = 0; i < NbMoy; i++ )
    {
        moyenne = moyenne + analogRead(A3);
    }
    moyenne = moyenne / NbMoy;
    Amp4 = (valeurBase[3] - moyenne ) / AmpMax;
    CarteOne[4] = Amp4;
    //Serial.print("\t Velo4:"); 
    Serial.print(Amp4,1);
    Serial.print(",");
//Velo 5
    moyenne = 0;
    for( i = 0; i < NbMoy; i++ )
    {
        moyenne = moyenne + analogRead(A4);
    }
    moyenne = moyenne / NbMoy;
    Amp5 = (valeurBase[4] - moyenne ) / AmpMax;
    CarteOne[5] = Amp5;
   // Serial.print("\t Velo5:"); 
    Serial.print(Amp5,1);
    Serial.println(",");
  delay(500);
}

void setup()
{
  Serial.begin(74880);
  
  int a = 1;
  int b = 2;
  
  if(a >= b)  //如果a>b，打印"a >= b"
  {
    Serial.printf("a >= b");
  }
  else        //否则，打印"a < b"
  {
    Serial.printf("a < b");
  }
}

void loop()
{
  
}

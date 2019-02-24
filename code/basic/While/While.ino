void setup()
{
  Serial.begin(74880);
  
  int a = 1;
  while(a <= 3)               //当a<=3这个条件为真时执行大括号的内容
  {
    Serial.printf("%d\n", a);//打印a的值并换行，\n是换行的意思
    a = a + 1;                //把a + 1的值赋值给a
  }
}

void loop()
{
  
}

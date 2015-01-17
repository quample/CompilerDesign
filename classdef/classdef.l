%option noyywrap
%{
#include "y.tab.h"
%}

%%
class {return CLASS;}
abstract {return ABSTRACT;}
public {return PUBLIC;}
protected {return PROTECTED;}
private {return PRIVATE;}
static {return STATIC;}
boolean {return BOOLEAN;}
char {return CHAR;}
byte {return BYTE;}
short {return SHORT;}
int {return INT;}
long {return LONG;}
float {return FLOAT;}
double {return DOUBLE;}
void {return VOID;}
[{] {return OPENFLOWER;}
[}] {return CLOSEFLOWER;}
[;] {return SEMICOLON;}
[,] {return COMMA;}
[(] {return OPENBRACE;}
[)] {return CLOSEBRACE;}
[a-zA-Z][a-zA-Z0-9_]* {return IDENTIFIER;}
[\t \n]+ ;

%%

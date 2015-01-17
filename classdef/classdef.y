%{
#include <stdio.h>
%}
%token CLASS IDENTIFIER ABSTRACT PUBLIC PROTECTED PRIVATE STATIC 
%token BOOLEAN CHAR BYTE SHORT INT LONG FLOAT DOUBLE VOID
%token OPENFLOWER CLOSEFLOWER SEMICOLON COMMA OPENBRACE CLOSEBRACE

%%
TypeDeclaration
	: ClassHeader OPENFLOWER FieldDeclarations CLOSEFLOWER
	| ClassHeader OPENFLOWER CLOSEFLOWER
	;
ClassHeader
	: Modifier CLASS IDENTIFIER
	|          CLASS IDENTIFIER
	;
Modifier
	: ABSTRACT
	| PUBLIC
	| PROTECTED
	| PRIVATE
	| STATIC
	;
FieldDeclarations
	: FieldDeclarationOptSemi
    | FieldDeclarations FieldDeclarationOptSemi
	;
FieldDeclarationOptSemi
    : FieldDeclaration
    | FieldDeclaration SemiColons
    ;
SemiColons
	: SEMICOLON
    | SemiColons SEMICOLON
    ;
FieldDeclaration
	: FieldVariableDeclaration SEMICOLON
	| MethodDeclaration
	| ConstructorDeclaration
    ;
FieldVariableDeclaration
	: Modifier TypeSpecifier VariableDeclarators
	|           TypeSpecifier VariableDeclarators
	;
VariableDeclarators
	: IDENTIFIER
	| VariableDeclarators COMMA IDENTIFIER
	;
TypeSpecifier
	: BOOLEAN
	| CHAR
	| BYTE
	| SHORT
	| INT
	| LONG
	| FLOAT
	| DOUBLE
	| VOID
	;
MethodDeclaration
	:Modifier TypeSpecifier MethodDeclarator MethodBody
	|          TypeSpecifier MethodDeclarator MethodBody
	;
MethodDeclarator
	: IDENTIFIER OPENBRACE ParameterList CLOSEBRACE
	| IDENTIFIER OPENBRACE CLOSEBRACE
	;
ParameterList
	: Parameter
	| ParameterList COMMA Parameter
	;

Parameter
	: TypeSpecifier IDENTIFIER
    ;
MethodBody
	: Block
	| SEMICOLON
	;
Block
	: OPENFLOWER LocalVariableDeclarationsAndStatements CLOSEFLOWER
	| OPENFLOWER CLOSEFLOWER
    ;

LocalVariableDeclarationsAndStatements
	: LocalVariableDeclarationStatement
	| LocalVariableDeclarationsAndStatements LocalVariableDeclarationStatement
	;

LocalVariableDeclarationStatement
	: TypeSpecifier VariableDeclarators SEMICOLON
	;

ConstructorDeclaration
	: Modifier ConstructorDeclarator Block
	|           ConstructorDeclarator Block
	;

ConstructorDeclarator
	: IDENTIFIER OPENBRACE ParameterList CLOSEBRACE
	| IDENTIFIER OPENBRACE CLOSEBRACE
	;

%%
#include <stdio.h>
extern int yylex();
extern int yyparse();
extern FILE *yyin;
int main(int argc, char **argv)
{
	yyin = fopen(argv[1], "r");
	if(!yyparse())
		printf("Valid.\n");
}

int yyerror()
{
	printf("Invalid.\n");
}

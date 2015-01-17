import ply.yacc as yacc
import ply.lex as lex
tokens = ('NUMBER', 'PLUS')
t_PLUS = r'\+'
t_ignore = ' \t'
def t_NUMBER(t) :
	'\d+'
	t.value = int(t.value)
	return t

def t_error(t):
    print("Illegal character '%s'" % t.value)
    a=len(t.value)
    t.lexer.skip(a)

def t_newline(t) :
	r'\n'
	t.lexer.lineno += 1

def p_TypeSpecifier(p):
	'''TypeSpecifier
		: TypeName
		| TypeName Dims'''
def p_TypeName(p):
	'''TypeName
	: PrimitiveType
	| QualifiedName'''

def p_ClassNameList(p):
	'''ClassNameList
        : QualifiedName
        | ClassNameList COMMA QualifiedName'''
def p_PrimitiveType(p):
	'''PrimitiveType
		: BOOLEAN
		| CHAR
		| BYTE
		| SHORT
		| INT
		| LONG
		| FLOAT
		| DOUBLE
		| String
		| Unit 
		| VAR 
		| VAL '''
def p_SemiColons(p):
	'''SemiColons
		: 'SEMICOLON'
        | SemiColons 'SEMICOLON' '''

def p_CompilationUnit(p):
	'''CompilationUnit
		: ProgramFile'''

def p_ProgramFile(p):
	'''ProgramFile
		: PackageStatement ImportStatements TypeDeclarations
		| PackageStatement ImportStatements
		| PackageStatement                  TypeDeclarations
		|                  ImportStatements TypeDeclarations
		| PackageStatement
		|                  ImportStatements
		|                                   TypeDeclarations '''

def p_PackageStatement(p):
	'''PackageStatement
		: PACKAGE QualifiedName SemiColons '''

def p_TypeDeclarations(p):
	'''TypeDeclarations
		: TypeDeclarationOptSemi
		| TypeDeclarations TypeDeclarationOptSemi ''' #nested classes

def p_TypeDeclarationOptSemi(p):
	'''TypeDeclarationOptSemi
		: TypeDeclaration
		| TypeDeclaration SemiColons'''
       
def p_ImportStatements(p):
	'''ImportStatements
		: ImportStatement
		| ImportStatements ImportStatement''' #multiple imports

def p_ImportStatement(p):
	'''ImportStatement
		: IMPORT QualifiedName SemiColons
		| IMPORT QualifiedName DOT UNDERSCORE SemiColons''' #import a._ format
	

def p_QualifiedName(p):
	''' QualifiedName
		: IDENTIFIER
		| QualifiedName DOT IDENTIFIER ''' #import a.a  format

def p_TypeDeclaration(p):
	''' TypeDeclaration
		: ClassHeader OPENBRACE FieldDeclarations CLOSEBRACE 
		| ClassHeader OPENBRACE CLOSEBRACE ''' #empty class

def p_ClassHeader(p):
	'''ClassHeader
		: ABSTRACT ClassWord IDENTIFIER Extends Interfaces
		| ABSTRACT ClassWord IDENTIFIER Extends
		| ABSTRACT ClassWord IDENTIFIER       Interfaces
		|          ClassWord IDENTIFIER Extends Interfaces
		| ABSTRACT ClassWord IDENTIFIER
		|           ClassWord IDENTIFIER Extends
		|           ClassWord IDENTIFIER       Interfaces
		|           ClassWord IDENTIFIER  
		| ABSTRACT ClassWord IDENTIFIER OPENPARA VariableDec CLOSEPARA
		| ClassWord IDENTIFIER OPENPARA VariableDec CLOSEPARA '''

def p_VariableDec(p):
	'''VariableDec
		: VAR IDENTIFIER COLON  PrimitiveType
		| VAL IDENTIFIER  COLON PrimitiveType
		| VariableDec VAR IDENTIFIER COLON  PrimitiveType'''

def p_ClassWord(p):
	'''ClassWord
		: CLASS
		| TRAIT 
		| OBJECT'''

def p_Interfaces(p):
	'''Interfaces
		: IMPLEMENTS ClassNameList '''

def p_Modifiers(p):
	'''Modifiers
		: Modifier
		| Modifiers Modifier '''
	
def p_Modifier(p):
	'''Modifier
		: ABSTRACT
		| FINAL
		| PRIVATE
		| STATIC
		| VAR 
		| VAL '''

def p_FieldDeclarations(p):
	'''FieldDeclarations
		: FieldDeclarationOptSemi
		| FieldDeclarations FieldDeclarationOptSemi '''
def p_FieldDeclaration(p):
	'''FieldDeclaration
		: FieldVariableDeclaration
		| MethodDeclaration
		| NonStaticInitializer
        | TypeDeclaration  '''
def p_FieldVariableDeclaration(p):
	'''FieldVariableDeclaration
		: Modifiers TypeSpecifier VariableDeclarators '''

def p_VariableDeclarators(p):
	'''VariableDeclarators
		: VariableDeclarator
		| VariableDeclarators ',' VariableDeclarator  '''
def p_VariableDeclarator(p):
	'''VariableDeclarator
		: DeclaratorName
		| DeclaratorName '=' VariableInitializer '''

def p_VariableInitializer(p):
	'''VariableInitializer
		: Expression '''

def p_DeclaratorName(p):
	'''DeclaratorName
		: IDENTIFIER
		| IDENTIFIER COLON PrimitiveType '''

def p_MethodDeclaration(p):
	'''MethodDeclaration
		: Modifiers DEF MethodDeclarator MethodBody
		|           DEF MethodDeclarator MethodBody  '''
def p_MethodDeclarator(p):
	'''MethodDeclarator
		: DeclaratorName OPENPARA ParameterList CLOSEPARA
		| DeclaratorName OPENPARA CLOSEPARA  '''
def p_ParameterList(p):
	'''ParameterList
		: Parameter
		| ParameterList COMMA Parameter  '''

def p_Parameter(p):
	'''Parameter
		: TypeSpecifier DeclaratorName
		| FINAL TypeSpecifier DeclaratorName  '''

def p_NonStaticInitializer(p):
	'''MethodBody
		: Block
		| SEMICOLON  '''
def p_NonStaticInitializer(p):
	'''NonStaticInitializer
		: Block  '''
def p_Block(p):
	'''Block
		: OPENBRACE LocalVariableDeclarationsAndStatements CLOSEBRACE
		| OPENBRACE CLOSEBRACE  '''

def p_LocalVariableDeclarationsAndStatements(p):
	'''LocalVariableDeclarationsAndStatements
		: LocalVariableDeclarationOrStatement
		| LocalVariableDeclarationsAndStatements LocalVariableDeclarationOrStatement  '''
def p_LocalVariableDeclarationOrStatement(p):
	'''LocalVariableDeclarationOrStatement
		: LocalVariableDeclarationStatement
		| Statement  '''
def p_LocalVariableDeclarationStatement(p):
	'''LocalVariableDeclarationStatement
		: TypeSpecifier VariableDeclarators SEMICOLON
        | FINAL TypeSpecifier VariableDeclarators SEMICOLON  '''
def p_Statement(p):
	'''Statement
		: EmptyStatement
		| ExpressionStatement 
		| SelectionStatement
		| IterationStatement
		| JumpStatement
		| Block  '''
def p_EmptyStatement(p):
	'''EmptyStatement
		: SEMICOLON  '''
def p_ExpressionStatement(p):
	'''ExpressionStatement
		: Expression '''

def p_SelectionStatement(p):
	'''SelectionStatement
		: IF OPENPARA Expression CLOSEPARA Statement
		| IF OPENPARA Expression CLOSEPARA Statement ELSE Statement
		| Expression MATCH  Block '''

def p_(p):
	'''IterationStatement
		: WHILE OPENPARA Expression CLOSEPARA Statement
		| DO Statement WHILE OPENPARA Expression CLOSEPARA SEMICOLON
		| FOR OPENPARA ForInit ForExpr ForIncr CLOSEPARA Statement
		| FOR OPENPARA ForInit ForExpr         CLOSEPARA Statement  '''
def p_ForInit(p):
	'''ForInit
		: ExpressionStatements SEMICOLON
		| LocalVariableDeclarationStatement
		| SEMICOLON  '''
def p_ForExpr(p):
	'''ForExpr
		: Expression SEMICOLON
		| SEMICOLON  '''
def p_ForIncr(p):
	'''ForIncr
		: ExpressionStatements '''
def p_ExpressionStatements(p):
	''' ExpressionStatements
		: ExpressionStatement
		| ExpressionStatements COMMA ExpressionStatement '''

def p_JumpStatement(p):
	''' JumpStatement
		: BREAK IDENTIFIER 
		| BREAK            
		| CONTINUE IDENTIFIER 
		| CONTINUE         
		| RETURN Expression 
		| RETURN '''
def p_(p):
	'''  '''
def p_(p):
	'''  '''
def p_(p):
	'''  '''
def p_(p):
	'''  '''
def p_(p):
	'''  '''
def p_(p):
	'''  '''
def p_(p):
	'''  '''
def p_(p):
	'''  '''
def p_(p):
	'''  '''
def p_(p):
	'''  '''
def p_(p):
	'''  '''
def p_(p):
	'''  '''
def p_(p):
	'''  '''
def p_(p):
	'''  '''










def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOI")

lexer = lex.lex()
parser = yacc.yacc()
#include <p24fj128ga010.h>

//Konfiguracja dla Explorer 16 z progr. icd2
_CONFIG1(JTAGEN_OFF & GCP_OFF & GWRP_OFF & BKBUG_OFF & COE_OFF & FWDTEN_OFF)
_CONFIG2(FCKSM_CSDCMD & OSCIOFNC_ON & POSCMOD_HS & FNOSC_PRI)

#define SCALE 308L

int main(void){
unsigned long i;
unsigned char display=0;
unsigned long licznik_grey = 0;
unsigned char display_for7 = 7;
unsigned char display_for8 = 1;
//inicjalizacja
 PORTA=0x0000;
 TRISA=0xFF00;
 TRISD=0xFFFF;

unsigned int x;
unsigned int y;
unsigned int temp = 0;
unsigned int is_jeden = 0;
unsigned int is_dwa = 0;
unsigned int is_trzy = 0;
unsigned int is_cztery = 0;
unsigned int is_piec = 0;
unsigned int is_szesc = 0;
unsigned int is_siedem =0;

int strona = 0;

zad1:
	display++;
	goto again;

zad2:
	display--;
	goto again;

zad3:
	licznik_grey++;
	display = licznik_grey ^ (licznik_grey >> 1);
	goto again;

zad4:
	licznik_grey--;
	display = licznik_grey ^ (licznik_grey >> 1);
	goto again;
	
zad5:
	licznik_grey++;
	x = (unsigned int)licznik_grey / 10;
	y = (unsigned int)licznik_grey % 10;
	display = (x << 4) | y;
	goto again;

zad6:
	licznik_grey--;
	x = (unsigned int)licznik_grey / 10;
	y = (unsigned int)licznik_grey % 10;
	display = (x >> 4) | y;
	goto again;

zad7:
	display = display_for7;
	if(strona == 0){
		display_for7 = display_for7 << 1;
	} else if(strona == 1){
		display_for7 = display_for7 >> 1;	
	}

	if(display_for7 == 224) strona = 1;
	else if(display_for7 == 7) strona = 0;
	goto again;

zad8:
	if(is_siedem == 1 && display_for8 == 255){
		is_siedem = 0;
		is_szesc = 0;
		is_piec = 0;
		is_cztery = 0;
		is_trzy = 0;
		is_dwa = 0;
		is_jeden = 0;
		display_for8 = display_for8 << 1;
		display_for8 = 1;
	}
	else if(is_siedem == 1){
		display_for8 = display_for8 << 1;
	}
	else if(is_szesc == 1 && display_for8 == 254){
		is_siedem = 1;
		display_for8 = display_for8 << 1;
		display_for8 = 1;
	}
	else if(is_piec == 1 && display_for8 == 252){
		is_szesc = 1;
		display_for8 = display_for8 << 1;
		display_for8 = 1;
	}
	else if(is_cztery == 1 && display_for8 == 248){
		is_piec = 1;
		display_for8 = display_for8 << 1;
		display_for8 = 1;
	}
	else if(is_trzy == 1 && display_for8 == 240){
		is_cztery = 1;
		display_for8 = display_for8 << 1;
		display_for8 = 1;
	}
	else if(is_dwa == 1 && display_for8 == 224){
		is_trzy = 1;
		display_for8 = display_for8 << 1;
		display_for8 = 1;
	}
	else if(is_jeden == 1 && display_for8 == 192){
		//is_jeden = 0;
		is_dwa = 1;
		display_for8 = display_for8 << 1;
		display_for8 = 1;
	} else if(display_for8 == 128){
		is_jeden = 1;
		display_for8 = display_for8 << 1;
		display_for8 = 1;
	} else {
		display_for8 = display_for8 << 1;
	}

	

	if(is_siedem){
		display_for8 = display_for8 | 254;
	}
	else if(is_szesc){
		display_for8 = display_for8 | 252;
	}
	else if(is_piec){
		display_for8 = display_for8 | 248;
	}
	else if(is_cztery){
		display_for8 = display_for8 | 240;
	}
	else if(is_trzy){
		display_for8 = display_for8 | 224;
	}
	else if(is_dwa){
		display_for8 = display_for8 | 192;
	}
	else if(is_jeden){
		display_for8 = display_for8 | 128;
	}
	display = display_for8;
	goto again;
 
unsigned char program = 0;
again:
	Nop();
	PORTA=(unsigned int) display;
	for(i=500L*SCALE;i>0;i--) Nop();
	if (PORTDbits.RD13 == 0){
		program++;
	}
	else if(PORTDbits.RD6 == 0){
		program--;
	}
	if(program < 0){
		program = 9;
	} else if(program > 9){
		program = 0;
	}
	if(program == 0){
		display = 0;
	} else if(program == 1){
		goto zad1;
	} else if(program == 2){
		goto zad2;
	}  else if(program == 3){
		goto zad3;
	} else if(program == 4){
		goto zad4;
	} else if(program == 5){
		goto zad5;
	} else if(program == 6){
		goto zad6;
	} else if(program == 7){
		goto zad7;
	} else if(program == 8){
		goto zad8;
	} else if(program == 9){
		display = 9;
	}

	goto again;
}

//piąety bit (17 >> 4) & 1

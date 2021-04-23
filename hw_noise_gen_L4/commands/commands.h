#include "main.h"

//General commands
#define STATE '0'
    //State commands
    #define ON '1'
    #define OFF '0'

#define ATTENUATION '1'

#define BAND '2'

#define RST '3'
    
//Actual parameters
extern uint8_t act_state;
extern float act_attenuation;
extern uint8_t act_band;

extern uint32_t num_norm_samp;

int ProcessRequest(uint8_t *, uint16_t);
int symb_to_num(uint8_t);

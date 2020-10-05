#include "commands.h"

//Actual parameters
uint8_t act_state = OFF;
uint8_t act_attenuation = 0;
uint8_t act_band = 0;

int ProcessRequest(uint8_t *buffer, uint16_t len)
{
    uint8_t result = 0;
    if(len == 2){
        switch(buffer[0])
	    {
            case STATE:
                if (buffer[1] == ON){
                    act_state = ON;
                    HAL_DAC_Start(&hdac,DAC_CHANNEL_1);
                }
                else
                {
                    act_state = OFF;
                    HAL_DAC_Stop(&hdac, DAC1_CHANNEL_1);
                }
            break;
            case ATTENUATION:
                act_attenuation = symb_to_num(buffer[1]);
            break;
            case BAND:
                act_band = symb_to_num(buffer[1]);
            break;
            default:
                result = 1;
        }
    }
    else
        result = 1;
    return result;
}

int symb_to_num(uint8_t symb){
    if ((symb >= 48) && (symb <= 57))
        return (symb - 48);
    
    if ((symb >= 97) && (symb <= 102))
        return (symb - 87);
    return -1;
}
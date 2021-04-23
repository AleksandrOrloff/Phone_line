#include "commands.h"

//Actual parameters
uint8_t act_state = OFF;
float act_attenuation = 3.1623;
uint8_t act_band = 0;

uint32_t num_norm_samp = 1000;

float db[9] = {3.1623, 4.4668, 6.3096, 8.9125, 12.5893, 17.7828, 25.1189, 35.4813, 50.1187};

int ProcessRequest(uint8_t *buffer, uint16_t len)
{
    uint8_t result = 0;
    if(len == 2){
        switch(buffer[0])
	    {
            case STATE:
                if (buffer[1] == ON){
                    act_state = ON;
                    HAL_DAC_Start(&hdac1,DAC_CHANNEL_2);
                }
                else
                {
                    act_state = OFF;
                    HAL_DAC_Stop(&hdac1, DAC1_CHANNEL_2);
                }
            break;
            case ATTENUATION:
                act_attenuation = db[symb_to_num(buffer[1])];
                num_norm_samp = 1000;
            break;
            case BAND:
                act_band = symb_to_num(buffer[1]);
                num_norm_samp = 1000;
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

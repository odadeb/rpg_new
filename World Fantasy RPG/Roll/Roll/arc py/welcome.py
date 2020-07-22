# -*- coding: utf-8 -*-
from dice import Diced20
class WelcomePlayer():
    en_welcome_01 = 'Welcome player, it is system to roll dice to your rpg'
    en_Welcome_02 =  'can i help you with something?'
    pt_bemvindo_01 = 'Benvindo jogador, esse é o sistema de rolagem para seu rpg'
    pt_bemvindo_02 = 'Como posso ajudar você?'
        
    def __init__(self, dice_type):
        self.dice_type = dice_type
        
        
    def rolagem(self):    
        if dice_type == '20':
            rolld20 = Dice.dice20
            print(f'O redultado da rolagem é: {rolld20}')
            
            
        elif dice_type == '8':            
                rolld08 == Dice.dice8
                print(f'O redultado da rolagem é: {rolld08}')
           
                
        elif dice_type == '6':
                rolld06 == Dice.dice6
                print(f'O redultado da rolagem é: {rolld06}')
        else:
            return   
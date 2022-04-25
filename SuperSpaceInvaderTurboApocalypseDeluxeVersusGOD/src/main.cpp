/*!
 *
 * @file    main.cpp
 * @author  RUBINI Thomas
 * @author  SIMAILA Djalim
 * @author  FABRE Lucas
 * @date    January 2022
 * @version 1.0
 * @brief  	main
 *
 * Welcome to SUPER Space Invader turbo apocalypse DX - VS GOD 
 * This little game was made in love by the glorious Thomas, the sublime Lucas, and the magnificent Djalim
 */

#include <iostream>
#include "game.h"
using namespace std;

int main(){
	DEBUG_MSG("Starting program")
	srand(time(NULL));

	Game g;
	g.managedGames();
	DEBUG_MSG("Finished program. Goodbye !")

    return 0;
}
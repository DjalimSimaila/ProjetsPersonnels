/*!
 *
 * @file    pixelManager.cpp
 * @author  RUBINI Thomas
 * @author  SIMAILA Djalim
 * @author  FABRE Lucas
 * @date    January 2022
 * @version 1.0
 * @brief    Manages screen display
 *
 */


#include "pixelManager.h"

using namespace std;

void PixelManager::loadSprites(vector<Task>& tasks){
	ADD_SPRITE_TASK(logo)
	ADD_SPRITE_TASK(menuBackground)
	ADD_SPRITE_TASK(gameBackground)
	ADD_SPRITE_TASK(rightHand)
}

void PixelManager::startFrame() const {
	window.clearScreen();
}

void PixelManager::endFrame() const {
	window.finishFrame();
}

unsigned PixelManager::getScreenHeight() const {
	return window.getWindowSize().getY();
}

unsigned PixelManager::getScreenWidth() const {
	return window.getWindowSize().getX();
}
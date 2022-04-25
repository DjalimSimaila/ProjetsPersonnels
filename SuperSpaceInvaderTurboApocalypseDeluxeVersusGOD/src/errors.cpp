/*!
 *
 * @file    configData.h
 * @author  RUBINI Thomas
 * @date    January 2022
 * @version 1.0
 * @brief   error handling
 *
 */

#include "errors.h"

using namespace std;

config_error::config_error(const string& msg) : runtime_error(msg) {

}
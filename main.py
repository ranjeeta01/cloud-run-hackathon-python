
# Copyright 2020 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import logging
import random
from flask import Flask, request

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

app = Flask(__name__)
moves = ['F', 'T', 'L', 'R']
direction = ['N','S','E','W']

@app.route("/", methods=['GET'])
def index():
    return "Let the battle begin!"



def checkNearestPlayer():

@app.route("/", methods=['POST'])
def move():
    request.get_data()
    logger.info(request.json)

    size = request.json['arena']['dims'] #dimensions of arena
    bots_state = request.json['arena']['state'] #state of the bots in arena
    mybot_link = data["_links"]["self"]["href"] # my bot link

    # {'x': 0, 'y': 0, 'direction': 'S', 'wasHit': False, 'score': 0} player response
    mybot = players_state[mybot_link] # to get own bot state
    amIHit = mybot["wasHit"]
    #bots_state.pop(bots_state) to remove my state from the dic
    
    possible_moves{
        'S': {
            'attack_moves': [[x, y-1], [x, y-2], [x, y-3]],
        }, 
        'N': {
            'attack_moves': [[x, y+1], [x, y+2], [x, y+3]],
        },
        'E': {
            'attack_moves': [[x+1, y], [x+2, y], [x+3, y]],
        },
        'W': {
            'attack_moves': [[x-1, y], [x-2, y], [x-3, y]],
        },  
    }

    def hitNearest(mybot):
        x=mybot['x']
        y=mybot['y']
        d1=[x+1,y]
        d2=[x+2,y]
        d3=[x+3,y]
        for i range(-3,3):
            if i==0:
                pass
            if [[x+i],y] in bots_state:
                return 'T'
            elif [x,y+i] in bots_state:
                return 'T'

    if amIHit=='True': #escape the block
        return 'F'
    else:
        hitNearest(mybot)
        
    
    # func to throw water and attack
    
#    for player in bots_state:
#        x,y=bots_state[player]
#        dirc = bots_state[player]['direction']

#        if mybot['x']==x and [x,abs(y-mybot['y'])] in possible_moves[mybot['direction']['attack_moves']]: #if player is in same row and attack dist
#            if mybot['direction']==direc:
#                return 'T'
#            else:
#                mybot['direction']=direc
#                return 'T'
        
#        elif mybot['x']==x and [x,abs(y+mybot['y'])] in possible_moves[mybot['direction']['attack_moves']]: #if player is in same row opp direc and attack dist
#            if mybot['direction']==direc:
#                return 'T'
#            else:
#                mybot['direction']=direc
#                return 'T'

#        elif mybot['y']==y and [abs(x+mybot['x']),y] in possible_moves[mybot['direction']['attack_moves']]: #if player is in same column opp direc and attack dist
#           if mybot['direction']==direc:
#                return 'T'
#            else:
#                mybot['direction']=direc
#                return 'T'

#        elif mybot['y']==y and [abs(x-mybot['x']),y] in possible_moves[mybot['direction']['attack_moves']]: #if player is in same column and attack dist
#            if mybot['direction']==direc:
#                return 'T'
#            else:
#                mybot['direction']=direc
#                return 'T'
                

#    return moves[random.randrange(len(moves))]

if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  

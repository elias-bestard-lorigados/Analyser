
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '17D073116A3E6DDE446CFF09EFA2F2D3'
    
_lr_action_items = {'OPEN_BRACKET':([0,3,4,14,22,23,],[3,5,3,5,5,5,]),'$end':([1,2,10,13,],[0,-2,-1,-3,]),'NEWLINE':([2,13,],[4,-3,]),'NUM':([3,5,14,15,16,22,23,],[9,11,9,18,19,9,9,]),'LABEL':([5,],[12,]),'CLOSE_BRACKET':([6,7,8,9,17,18,19,20,21,24,25,],[13,-4,-5,-7,-6,20,21,-9,-11,-8,-10,]),'COMMA':([9,11,12,20,21,],[14,15,16,22,23,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,4,],[1,10,]),'expression':([0,4,],[2,2,]),'generator':([3,14,22,23,],[6,17,24,25,]),'pairs':([3,14,22,23,],[7,7,7,7,]),'numbers':([3,14,22,23,],[8,8,8,8,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> expression NEWLINE start','start',3,'p_start','series_list_gramar.py',46),
  ('start -> expression','start',1,'p_start','series_list_gramar.py',47),
  ('expression -> OPEN_BRACKET generator CLOSE_BRACKET','expression',3,'p_expression','series_list_gramar.py',57),
  ('generator -> pairs','generator',1,'p_generator','series_list_gramar.py',62),
  ('generator -> numbers','generator',1,'p_generator','series_list_gramar.py',63),
  ('numbers -> NUM COMMA generator','numbers',3,'p_numbers','series_list_gramar.py',68),
  ('numbers -> NUM','numbers',1,'p_numbers','series_list_gramar.py',69),
  ('pairs -> OPEN_BRACKET NUM COMMA NUM CLOSE_BRACKET COMMA generator','pairs',7,'p_pairs','series_list_gramar.py',77),
  ('pairs -> OPEN_BRACKET NUM COMMA NUM CLOSE_BRACKET','pairs',5,'p_pairs','series_list_gramar.py',78),
  ('pairs -> OPEN_BRACKET LABEL COMMA NUM CLOSE_BRACKET COMMA generator','pairs',7,'p_pairs','series_list_gramar.py',79),
  ('pairs -> OPEN_BRACKET LABEL COMMA NUM CLOSE_BRACKET','pairs',5,'p_pairs','series_list_gramar.py',80),
]

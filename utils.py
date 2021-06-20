import numpy as np

class POVRayObject():
    def __init__(self, object_inicialization):
        self.obj_init = object_inicialization
        self.objects = []
        self.movements = []
        self.attributes = []

    def add_object(self, object_):
        '''
        Adiciona um objeto filho ao objeto
        '''

        self.objects.append(object_)

    def add_attribute(self, attribute: str):
        '''
        Adiciona atributo ao objeto
        '''
        self.attributes.append(attribute) 

    def add_pigment(self, pigment_value: str):
        '''
        Adiciona pigmento ao objeto
        '''
        pigment_str = 'pigment {{{}}}'.format(pigment_value)

        self.attributes.append(pigment_str)

    def add_rotation_y(self, rotate_angle: float, center_position: tuple):
        '''
        Translada o objeto para o centro, rotaciona ele, e translada para a posição incial novamente
        '''
        center_position = np.array(center_position)
        translate_string = 'translate <{:.2f}, {:.2f}, {:.2f}>'
        translate_start_str = translate_string.format(*(-center_position))
        translate_end_str = translate_string.format(*center_position)
        rotation_str = 'rotate <0, {:.2f}, 0>'.format(rotate_angle)

        self.movements.extend([
            translate_start_str,
            rotation_str,
            translate_end_str
        ])
    
    def str_with_tabs(self, string, tab_spaces):
        '''
        Retorna string com 'tab_spaces' tabs no começo
        '''
        return ('\t' * tab_spaces) + string

    def show_object_list(self, tab_spaces = 0):
        '''
        Retorna uma lista em que cada elemento é uma linha
        de comando em POVRay
        '''

        obj_str_list = []

        obj_init_str = '{} {{'.format(self.obj_init)
        obj_inicialization = self.str_with_tabs(
            obj_init_str,
            tab_spaces
        )

        obj_str_list.append(obj_inicialization)

        for object_ in self.objects:
            obj_str_list.extend(object_.show_object_list(tab_spaces + 1))

        for movement in self.movements:
            obj_str_list.append(self.str_with_tabs(movement, tab_spaces + 1))

        for attribute in self.attributes:
            obj_str_list.append(self.str_with_tabs(attribute, tab_spaces + 1))

        obj_str_list.append(
            self.str_with_tabs('}', tab_spaces)
        )

        return obj_str_list

    def show_object(self):
        '''
        Mostra toda a lista de comandos em POVRay
        '''

        obj_list_str = self.show_object_list()
        for line in obj_list_str:
            print(line)

class Union(POVRayObject):
    def __init__(self):
        super().__init__('union')

class Box(POVRayObject):
    def __init__(self, start_point, end_point):
        super().__init__('box')
        # Ponto inicial e ponto final da caixa
        points_str = '<{:.2f}, {:.2f}, {:.2f}>, <{:.2f}, {:.2f}, {:.2f}>'.format(
            *start_point,
            *end_point
        )
        self.add_attribute(points_str)

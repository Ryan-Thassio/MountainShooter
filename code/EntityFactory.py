from code.Background import Background

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'bg':
                list_bg = []
                for i in range(10):
                    list_bg.append(Background(f'bg{i}', position))
                    list_bg.append(Background(f'bg{i}', (800, 0)))
                return list_bg



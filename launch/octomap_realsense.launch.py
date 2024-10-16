from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Lançar o OctoMap Server
        Node(
            package='octomap_server',
            executable='octomap_server_node',
            name='octomap_server',
            output='screen',
            parameters=[{
                'resolution': 0.05,  # Ajuste a resolução conforme necessário
                'max_range': 10.0,  # Alcance máximo de 5 metros
                'queue_size': 100000,  # Tamanho da fila ajustado para lidar com grandes nuvens de pontos
                'frame_id': 'map',  # Frame de referência do OctoMap
                'latch': False,  # Publica a mensagem e mantém latched para novos assinantes
                'octomap_publish_period': 0.2  # Publica atualizações a cada 0.5 segundos
            }],
            remappings=[
                ('/cloud_in', '/camera/camera/depth/color/points')  # Usando a nuvem de pontos publicada pela RealSense
            ]
        ),
    ])

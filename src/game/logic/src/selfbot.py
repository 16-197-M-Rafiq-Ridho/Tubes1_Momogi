# Maxavier Girvanus Manurung (123140191)
# Gilang Surya Agung (123140187)
# Muhammad Rafiq Ridho (123149197)
# kelompok 4 Momogi

from typing import Tuple, List
import math
from game.models import Board, GameObject, Position
from game.logic.base import BaseLogic

class MyBot(BaseLogic):
    def __init__(self):
        self.teleporters: List[GameObject] = []  # menyimpan data teleport
        self.teleport_pairs = {}  # menyimpan data pasangan teleport
    # fungsi untuk menentukan langkah selanjutnya
    def next_move(self, bot: GameObject, board: Board) -> Tuple[int, int]:
        current_pos = bot.position # mengambil posisi bot saat ini
        props = bot.properties # mengambil proprti dari bot
        
        if not self.teleporters:
            self.init_teleporters(board)
        
        if props.diamonds == props.inventory_size: # kembali ke base jika inventory penuh
            return self.move_to_base(current_pos, props.base, board)
        
        target_diamond = self.find_target_diamond(bot, board) # menemukan diamond terdekat
        if target_diamond:
            return self.move_to_diamond(current_pos, target_diamond.position, board)
        else:
            return self.move_to_base(current_pos, props.base, board) # Jika tidak ada diamond yang ditemukan, bergerak ke arah base

    def init_teleporters(self, board: Board) -> None: #
        self.teleporters = [obj for obj in board.game_objects if obj.type == "TeleportGameObject"]
        
        if len(self.teleporters) >= 2:
            self.teleport_pairs = {
                self.teleporters[0].id: self.teleporters[1],
                self.teleporters[1].id: self.teleporters[0]
            }
    # fungsi untuk kembali ke base
    def move_to_base(self, current_pos: Position, base_pos: Position, board: Board) -> Tuple[int, int]: 
        for tele in self.teleporters: # mencari teleport yang ada
            if tele.id in self.teleport_pairs:
                tele_dest = self.teleport_pairs[tele.id]  #
                if self.distance(tele_dest.position, base_pos) < self.distance(current_pos, base_pos):
                    if self.is_adjacent(current_pos, tele.position):
                        return self.direction_to(current_pos, tele.position)
        return self.safe_move(current_pos, base_pos, board)

    # fungsi untuk bergerak ke diamond terdekat
    def move_to_diamond(self, current_pos: Position, diamond_pos: Position, board: Board) -> Tuple[int, int]:
        for tele in self.teleporters: # mencari pasangan teleport untuk bergerak ke diamond
            if tele.id in self.teleport_pairs:
                tele_dest = self.teleport_pairs[tele.id]
                if self.distance(tele_dest.position, diamond_pos) < self.distance(current_pos, diamond_pos): # menghitung jarak menggunakan tele dan tidak
                    if self.is_adjacent(current_pos, tele.position): 
                        return self.direction_to(current_pos, tele.position) # bergerak ke teleport
        return self.safe_move(current_pos, diamond_pos, board) # bergerak ke diamond terdekat tanpa tele jika tidak ada tele terdekat

    def find_target_diamond(self, bot: GameObject, board: Board) -> GameObject: # fungsi untuk mencari diamond
        diamonds = [d for d in board.diamonds if not d.properties.pair_id] 
        
        if bot.properties.diamonds >= 4: # jika inventory berisi 4 maka bot mengambil diamon biru saja
            diamonds = [d for d in diamonds if d.properties.points == 1]
        
        return min(diamonds, key=lambda d: self.distance(bot.position, d.position)) if diamonds else None
    # fungsi bot untuk bergerak kanan kiri atas atau bawah
    def safe_move(self, current_pos: Position, target_pos: Position, board: Board) -> Tuple[int, int]:
        dx = 1 if target_pos.x > current_pos.x else -1 if target_pos.x < current_pos.x else 0 # bergerak ke atas atau bawah
        dy = 1 if target_pos.y > current_pos.y else -1 if target_pos.y < current_pos.y else 0 # bergerak ke kiri atau kanan
        # melakukan validasi gerakan valid atau tidak
        if abs(target_pos.x - current_pos.x) > abs(target_pos.y - current_pos.y):
            dy = 0
        else:
            dx = 0
        
        if not board.is_valid_move(current_pos, dx, dy):
            if dx != 0:
                dy = 1 if target_pos.y > current_pos.y else -1 if target_pos.y < current_pos.y else 0
                dx = 0
            else:
                dx = 1 if target_pos.x > current_pos.x else -1 if target_pos.x < current_pos.x else 0
                dy = 0
        
        return self.validate_move(current_pos, dx, dy, board)
    
    def validate_move(self, pos: Position, dx: int, dy: int, board: Board) -> Tuple[int, int]:
        valid_moves = {(1,0), (0,1), (-1,0), (0,-1)}
        if (dx, dy) in valid_moves and board.is_valid_move(pos, dx, dy): # melakukan validasi gerakan apakah di perbolehkan atau tidak
            return (dx, dy)
        
        for move in valid_moves: # melakukan iterasi semua gerakan dan mengambil gerakan yang valid
            if board.is_valid_move(pos, move[0], move[1]):
                return move
        return (0, 0) # tidak bergerak jika tidak valid
    # menghitung jarak teleport 
    def distance(self, pos1: Position, pos2: Position) -> float: 
        return math.sqrt((pos1.x - pos2.x)**2 + (pos1.y - pos2.y)**2)

    def is_adjacent(self, pos1: Position, pos2: Position) -> bool:
        return abs(pos1.x - pos2.x) + abs(pos1.y - pos2.y) == 1
    # menghitung jarak dari posisi sekarang ke posisi target
    def direction_to(self, current_pos: Position, target_pos: Position) -> Tuple[int, int]:
        dx = target_pos.x - current_pos.x
        dy = target_pos.y - current_pos.y
        return (dx, dy) if self.is_adjacent(current_pos, target_pos) else (0, 0)
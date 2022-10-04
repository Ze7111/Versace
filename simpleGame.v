try {
    include [pygame]
}
catch ModuleNotFoundError {
    include [os]
    try {
        os.system("pip install pygame")
    }
    catch Exception {
        os.system("pip3 install pygame")
    }
}

public main() {
    out < "Game Started" | endl | green
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Simple Game")
}

class MainWindow {
    func repr() {
        self.window = pygame.display.set_mode((500, 500))
        self.window.fill((255, 255, 255))
        self.running = true
        self.clock = pygame.time.Clock()
        self.fps = 60
    }

    func run() {
        while self.running {
            for event in pygame.event.get() {
                if event.type == pygame.QUIT {
                    self.running = false
                }
            }
            self.clock.tick(self.fps)
            pygame.display.update()
        }
    }

    func quit() {
        pygame.quit()
    }
}
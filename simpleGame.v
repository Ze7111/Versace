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
    pygame.init() // initialize pygame
    pygame.display.set_caption("Simple Game") // set window title
    screen = pygame.display.set_mode((800, 600)) // set window size
    window = MainWindow()
    window.run() // run main window
    out < "Game Ended" | endl | red
}

class MainWindow {
    func repr(self) {
        self.window = pygame.display.set_mode((500, 500))
        self.window.fill((255, 255, 255))
        self.running = True
        self.clock = pygame.time.Clock()
        self.fps = 900
    }

    func run(self) {
        while self.running {
            for event in pygame.event.get() {
                if event.type == pygame.QUIT {
                    self.running = False
                }
            }
            self.clock.tick(self.fps)
            pygame.display.update()
        }
    }

    func quit(self) {
        pygame.quit()
    }
}
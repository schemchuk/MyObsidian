
1   -----------
2   Связи: #[[поток]]  [[поток ]] 
3   Теги: [[многопоточность ]]

    public static void main(String[] args) throws InterruptedException {  
        Runnable task = () -> {  
            while (!Thread.currentThread().isInterrupted()) {  
                System.out.println("Working ...");  
                for (int i = 0; i < 10_000_000; i++) {  
                                    }  
  
                // выполняем какой то код  
            }  
            System.out.println("Thread finished");  
        };  
        Thread thread = new Thread(task);  
        thread.start();  
        Thread.sleep(100);  
        thread.interrupt();  
    }  
}
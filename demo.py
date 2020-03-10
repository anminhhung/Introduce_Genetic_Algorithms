import random 
  
SIZE = 100
GENES = '''
            abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP 
            QRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}
        '''
  
TARGET = "An_Minh_Hung 17520531"
  
class Individual(object): 

    def __init__(self, chromosome): 
        self.chromosome = chromosome  
        self.fitness = self.cal_fitness() 
  
    @classmethod
    def mutated_genes(self): 

        return random.choice(GENES) 
  
    @classmethod
    def create_gnome(self): 
        gnome_len = len(TARGET) 
        return [self.mutated_genes() for _ in range(gnome_len)] 
  
    def mate(self, par2): 
        child_chromosome = [] 
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):     
            prob = random.random() 

            if prob < 0.45: 
                child_chromosome.append(gp1) 
            elif prob < 0.90: 
                child_chromosome.append(gp2) 
            else: 
                child_chromosome.append(self.mutated_genes()) 
  
        return Individual(child_chromosome) 
  
    def cal_fitness(self): 
        # Tính số ký tự sai khác với TARGET (fitness score)
        fitness = 0
        for gs, gt in zip(self.chromosome, TARGET): 
            if gs != gt: fitness+= 1
        return fitness 
  
def main(): 
    generation = 1
    population = [] 
  
    for _ in range(SIZE): 
        gnome = Individual.create_gnome() 
        population.append(Individual(gnome)) 

    while True: 
        population = sorted(population, key = lambda x:x.fitness) 

        if population[0].fitness <= 0: 
            break

        new_generation = [] 
  
        # Lấy 10% cá thể mạnh nhất
        s = int((10*SIZE)/100) 
        new_generation.extend(population[:s]) 
  
        # Lấy 50% cá thể tiếp theo tạo cá thể mới  
        s = int((90*SIZE)/100) 
        for _ in range(s): 
            parent1 = random.choice(population[:50]) 
            parent2 = random.choice(population[:50]) 
            child = parent1.mate(parent2) 
            new_generation.append(child) 
  
        population = new_generation 
  
        print("Generation: {}\tString: {}\tFitness: {}".
              format(generation, "".join(population[0].chromosome), population[0].fitness)) 
  
        generation += 1
  
      
    print("Generation: {}\tString: {}\tFitness: {}".
          format(generation, "".join(population[0].chromosome), population[0].fitness)) 
  
if __name__ == '__main__': 
    main() 
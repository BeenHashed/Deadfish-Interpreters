class DeadFish 
{
    static void Main(string[] args) 
    {
        string file = args[0];
        if(File.Exists(file)) 
        {
            int accumulator = 0;
            string code = File.ReadAllText(file);
            for(int i = 0; i < code.Length; i++)
            {
                switch(code[i])
                {
                    case 'i':
                        accumulator++;
                        break;
                    case 'd':
                        accumulator--;
                        break;
                    case 's':
                        accumulator *= accumulator;
                        break;
                    case 'o':
                        Console.Write($"{accumulator} ");
                        break;
                }
            }

        }
        else 
        {
            Console.WriteLine("File was not found");
        }

    }
}
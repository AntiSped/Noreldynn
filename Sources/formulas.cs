using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

class OniFormulas {

    public static int Vitality(int level_modifier, int brawn, int toughness, int power_level) {

        return((50*level_modifier)+(5*(brawn+toughness)*power_level));

    }
    static void Main(string[] args){

        int test = Vitality(level_modifier: 3578, brawn: 1114, toughness: 167, power_level: 125);
        Console.WriteLine(test);
    }
}

public class WerewolfFormulas{}

public class ManawraithFormulas{}

public class KitsuneFormulas{}

public class DrakenFormulas{}
    
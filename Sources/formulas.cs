using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

public class Formulas 
{

    public static double Vitality(double level_modifier, int brawn, int toughness, int power_level) 
    {

        return ((50 * level_modifier) + (5 * (brawn + toughness) * power_level));

    }

    public static double Aether(double knowledge)
    {

        return (1000 * (1 + (0.0005 * knowledge)));

    }

    public static double magicArmor(double vitality, double mana_armor_amount) 
    {

        return (vitality * mana_armor_amount);

    }

    public static double physicalStat(double level_modifier, double dexterity, double brawn, double power_level)
    {

        return ((10 * level_modifier) + (1 * (dexterity + brawn) * power_level));

    }

    public static double arcanaStat(double level_modifier, double dexterity, double knowledge, double power_level)
    {

        return ((10 * level_modifier) + (1 * (dexterity + knowledge) * power_level));

    }

    public static double Defense(double level_modifier, double brawn, double toughness, double power_level)
    {

        return ((10 * level_modifier) + (1 * (brawn + toughness) * power_level));

    }

    public static double magicResist(double level_modifier, double knowledge, double toughness, double power_level)
    {

        return ((10 * level_modifier) + (1 * (knowledge + toughness) * power_level));

    }

    static void Main(string[] args)
    {

        double vitality = Vitality(level_modifier: 3578.5262, brawn: 1114, toughness: 167, power_level: 125);
        Console.WriteLine(vitality);

        double aether = Aether(knowledge: 1504);
        Console.WriteLine(aether);
    }
}

public class OniAttributes {}

public class WerewolfFormulas{}

public class ManawraithFormulas{}

public class KitsuneFormulas{}

public class DrakenFormulas{}
    
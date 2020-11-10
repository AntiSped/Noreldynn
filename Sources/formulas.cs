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
}

public class OniAttributes 
{
    
    public static double Brawn(double power_level)
    {
        double val = Math.Pow(0.7 + (0.175 * power_level), 2.25);
        return (3.5 + (val));

    }

    public static double Knowledge(double power_level)
    {
        double val = Math.Pow(0.8 + (0.2 * power_level), 2.25);
        return (4 + val);
    }

    public static void Main(string[] args)
    {
        Formulas formulaObject = new Formulas();

        Console.WriteLine(Knowledge(power_level: 125));
    }
}

public class WerewolfFormulas{}

public class ManawraithFormulas{}

public class KitsuneFormulas{}

public class DrakenFormulas{}
    
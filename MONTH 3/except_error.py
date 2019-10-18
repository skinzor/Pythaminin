except IOError:
    print('An error occured trying to read the file.')
    
except ValueError:
    print('Non-numeric data found in the file.')

except ImportError:
    print "NO module found"
    
except EOFError:
    print('Why did you do an EOF on me?')

except KeyboardInterrupt:
    print('You cancelled the operation.')

except:
    print('An error occured.')

from module import prediction_save
import argparse





if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--i', type = str, help='please image -input')
    parser.add_argument('--o', type = str, help='please image -input')
    args = parser.parse_args()
    path = prediction_save(args.i, args.o)

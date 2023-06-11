import {
  IconButton,
  Text,
  Flex,
  Spacer,
  Grid,
  GridItem,
} from "@chakra-ui/react";
import { FiSettings } from "react-icons/fi";
import { TokenDisplay } from "./TokenDisplay";

const backgroundUrl =
  "https://www.myfreetextures.com/wp-content/uploads/2012/05/2011-06-11-09606.jpg";

export const Game = () => {
  return (
    <Grid
      opacity="0.7"
      background={`url(${backgroundUrl})`}
      padding="4"
      h="100vh"
      w="full"
      templateColumns="48px 1fr 48px"
      templateRows="64px 1fr 48px"
      templateAreas={`
      "player action opponent"
      "player table opponent"
      "player rack opponent"
      `}
    >
      <GridItem border="1" area="player">
        <Flex gap="2" direction="column" h="full" align="center">
          <TokenDisplay
            player={{ name: "E", color: "red" }}
            tokens={[{ name: "A" }, { name: "B" }, { name: "C" }]}
          />
        </Flex>
      </GridItem>
      <GridItem border="1" area="action">
        <Flex justify="center" align="center">
          <Text fontWeight="bold" fontSize="3xl" color="black">
            Where current action is displayed
          </Text>
        </Flex>
      </GridItem>
      <GridItem border="1" area="opponent">
        <Flex gap="2" direction="column" h="full" align="center">
          <TokenDisplay
            player={{ name: "J", color: "green" }}
            tokens={[
              { name: "W" },
              { name: "X" },
              { name: "Y" },
              { name: "Z" },
            ]}
          />
          <Spacer />
          <IconButton
            aria-label="settings"
            size="lg"
            backgroundColor="blue.600"
            icon={<FiSettings />}
          />
        </Flex>
      </GridItem>
      <GridItem border="1" area="table">
        <Flex h="full" justify="center" align="center">
          Table
        </Flex>
      </GridItem>
      <GridItem border="1" area="rack">
        <Flex h="full" justify="center" align="center">
          <Text fontWeight="bold" fontSize="3xl" color="gray.900">
            Where cards in player's rack are displayed
          </Text>
        </Flex>
      </GridItem>
    </Grid>
  );
};